function ___(__)
  local __=__ or {_=1,__=#_}
  if __.__-__._<1 then
    return
  end
  _.__=_[__._]
  _._=__._
  _.___=__.__
  for __=_._+1,__.__ do
    ::_::
    if _.__>_[__] then
      _[_._] = _[__]
      _[__] = _.__
      _._=__
    else
      for ___=_.___,__+1,-1 do
        if _[___]<=_.__ then
          _._=_[___]
          _[___] = _[__]
          _[__] = _._
          _._ = __-1
          _.___=___-1
          goto _
        end
      end
      goto __
    end
  end
  ::__::
  ___({_=__._,__=_._-1})
  ___({_=_._+1,__=__.__})
end
_={}
_.____={}
for __ in io.lines("./2024/day_01/input/input.txt") do
  for ___ in string.gmatch(__, "([^%s]+)") do
    if #_==#_.____ then
      table.insert(_,tonumber(___))
    else
      table.insert(_.____,tonumber(___))
    end
  end
end
___()
____={}
for ___,__ in ipairs(_) do
  ____[___]=__
end
_=_.____
___()
___=0
for _,__ in ipairs(_) do
  if ____[_]-__>0 then
    ___=___+____[_]-__
  else
    ___=___+__-____[_]
  end
end
print(___)
