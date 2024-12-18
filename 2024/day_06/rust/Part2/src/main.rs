use std::collections::HashSet;
use std::fs::File;
use std::hash::{Hash, Hasher};
use std::io::{self, BufRead, BufReader, Read};
use std::iter::successors;

#[derive(Clone, Copy, Default, Debug, PartialEq, Eq, Hash)]
enum Orientation {
    #[default]
    Forward,
    Right,
    Backward,
    Left,
}

impl Orientation {
    pub const fn turn_left(self) -> Self {
        match self {
            Self::Forward => Self::Right,
            Self::Right => Self::Backward,
            Self::Backward => Self::Left,
            Self::Left => Self::Forward,
        }
    }
}

#[derive(Clone, Copy, Default, Debug, PartialEq, Eq, Hash)]
struct Point {
    x: isize,
    y: isize,
}

impl Point {
    const fn is_in_frame(&self, max_c: &Point) -> bool {
        0 <= self.x && self.x <= max_c.x && 0 <= self.y && self.y <= max_c.y
    }
}

#[derive(Clone, Copy, Default, Debug, PartialEq, Eq, Hash)]
struct Position {
    coords: Point,
    direction: Orientation,
}

impl Position {
    pub const fn turn_left(self) -> Self {
        Self {
            direction: self.direction.turn_left(),
            ..self
        }
    }

    const fn step(mut self) -> Self {
        match self.direction {
            Orientation::Forward => {
                self.coords.y -= 1;
            }
            Orientation::Right => {
                self.coords.x += 1;
            }
            Orientation::Backward => {
                self.coords.y += 1;
            }
            Orientation::Left => {
                self.coords.x -= 1;
            }
        }

        self
    }

    fn next_valid_position(
        self,
        mut is_valid: impl FnMut(&Point) -> bool,
        is_within_limits: impl FnOnce(&Point) -> bool,
    ) -> Option<Self> {
        successors(Some(self), |position| Some(position.turn_left()))
            .take(4)
            .map(Self::step)
            .find(|position| is_valid(&position.coords))
            .filter(|position| is_within_limits(&position.coords))
    }
}

#[derive(Clone, Default, Debug)]
struct WalkState {
    past: HashSet<Position>,
    guard: Position,
}

impl WalkState {
    fn hits_loop<P1, P2>(self, is_valid: P1, is_within_limits: P2) -> bool
    where
        P1: Copy + FnMut(&Point) -> bool,
        P2: Copy + FnOnce(&Point) -> bool,
    {
        let Self { mut past, guard } = self;

        successors(Some(guard), |guard| {
            guard.next_valid_position(is_valid, is_within_limits)
        })
        .any(|guard| !past.insert(guard))
    }
}

#[derive(Default, Debug)]
struct Grid {
    obstacles: HashSet<Point>,
    guard_start: Position,
    max_c: Point,
}

#[derive(Debug)]
pub enum ParseError {
    Io(io::Error),
    WrongFormat,
    NoGuard,
    MoreThanOneGuard,
}

impl From<io::Error> for ParseError {
    fn from(err: io::Error) -> Self {
        Self::Io(err)
    }
}

fn parse<T: Read>(reader: BufReader<T>) -> Result<Grid, ParseError> {
    let mut obstacles = HashSet::<Point>::new();
    let mut guard_start = None;
    let mut max_c = Point::default();
    for (l, y) in reader.lines().zip(0..) {
        for (c, x) in l?.chars().zip(0..) {
            let coords = Point { x, y };
            match c {
                '.' => (),
                '#' => {
                    obstacles.insert(coords);
                }
                '^' => {
                    if guard_start.is_some() {
                        return Err(ParseError::MoreThanOneGuard);
                    }

                    guard_start = Some(Position {
                        coords,
                        ..Default::default()
                    });
                }
                _ => return Err(ParseError::WrongFormat),
            }
            max_c = coords;
        }
    }

    if let Some(guard_start) = guard_start {
        Ok(Grid {
            obstacles,
            guard_start,
            max_c,
        })
    } else {
        Err(ParseError::NoGuard)
    }
}

#[derive(Debug)]
struct WalkStateDeviation {
    new_obstacle: Point,
    state: WalkState,
}

impl PartialEq for WalkStateDeviation {
    fn eq(&self, other: &Self) -> bool {
        self.new_obstacle == other.new_obstacle
    }
}

impl Eq for WalkStateDeviation {}

impl Hash for WalkStateDeviation {
    fn hash<H: Hasher>(&self, state: &mut H) {
        self.new_obstacle.hash(state);
    }
}

fn get_possible_deviations(
    field: &Grid,
    mut state: WalkState,
) -> (HashSet<WalkStateDeviation>, Option<Position>) {
    let mut main_path_loop_position = None;

    let mut possible_deviations = HashSet::<WalkStateDeviation>::new();
    while let Some(next_position) = state.guard.next_valid_position(
        |coords| !field.obstacles.contains(coords),
        |coords| coords.is_in_frame(&field.max_c),
    ) {
        {
            let deviation = WalkStateDeviation {
                new_obstacle: next_position.coords,
                state: state.clone(),
            };

            possible_deviations.insert(deviation);
        }

        if !state.past.insert(state.guard) {
            main_path_loop_position = Some(state.guard);
            break;
        }

        state.guard = next_position;
    }
    let deviation_in_starting_point = WalkStateDeviation {
        new_obstacle: field.guard_start.coords,
        state: Default::default(),
    };
    possible_deviations.remove(&deviation_in_starting_point);

    (possible_deviations, main_path_loop_position)
}

fn deviation_loops(field: &Grid, deviations: HashSet<WalkStateDeviation>) -> usize {
    deviations
        .into_iter()
        .filter_map(|deviation| {
            if deviation.state.hits_loop(
                |coords| coords != &deviation.new_obstacle && !field.obstacles.contains(coords),
                |coords| coords.is_in_frame(&field.max_c),
            ) {
                Some(deviation.new_obstacle)
            } else {
                None
            }
        })
        .count()
}

fn solve(field: &Grid) -> usize {
    let init_state = WalkState {
        guard: field.guard_start,
        ..Default::default()
    };

    let (possible_deviations, main_path_loop_position) = get_possible_deviations(field, init_state);

    deviation_loops(field, possible_deviations)
        + if main_path_loop_position.is_some() {
            1
        } else {
            0
        }
}

fn main() -> Result<(), ParseError> {
    let field = parse(BufReader::new(File::open("input.txt")?))?;
    let solution = solve(&field);

    println!("{solution}");

    Ok(())
}
