<?php
//sorry in advance for the bad variables i was converting this from TIBASIC
function isInt($value){
    if (is_int($value)){
        return true;
    } else{
        return false;
    }
}
function triForC($a, $b){
    if (!isInt($a) and !isInt($b)){
        return false;
    }
    $output = $a**2+$b**2;
    return $output;
}
function triForB($a,$c){
    if (!isInt($a) and !isInt($c)){
        return false;
    }
    $output = sqrt(($c**2)-($a**2));
    return $output;
}
function triForC3D($l,$w,$h){
    if (!isInt($l) and !isInt($w) and !isInt($h)){
        return false;
    }
    $output = sqrt((sqrt(($l**2)+($w**2))**2)+($h**2));
    return $output;
}
function vertOfPorab($a, $b, $c){
    if (!isInt($a) and !isInt($b) and !isInt($c)){
        return false;
    }
    $xVrt = (-($b))/(2*($a));
    $yVrt = ($a*($xVrt)**2)+($b*($xVrt))+($c);
    return [$xVrt, $yVrt];
}
function pointOnPorab($x, $a, $b, $c){
    if (!isInt($a) and !isInt($b) and !isInt($c) and !isInt($x)){
        return false;
    }
    $c = $c-$x;
    $topPlus = -($b)+sqrt($b**2 - (4*($a)*($c)));
    $botPlus = (2*($a));
    $topMins = -($b)-sqrt($b**2 - 4*($a)*($c));
    $botMins = (2*($a));
    return [[($topPlus/$botPlus), $x], [($topMins/$botMins), -$x]];
}
?>