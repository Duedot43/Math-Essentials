//sorry in advance for the bad variables i was converting this from TIBASIC
function isInt(value){
    if (is_int(value)){
        return true;
    } else{
        return false;
    }
}
function triForC(a, b){
    if (!isInt(a) && !isInt(b)){
        return false;
    }
    var output = a**2+b**2;
    return output;
}
function triForB(a,c){
    if (!isInt(a) && !isInt(c)){
        return false;
    }
    var output = sqrt((c**2)-(a**2));
    return output;
}
function triForC3D(l,w,h){
    if (!isInt(l) && !isInt(w) && !isInt(h)){
        return false;
    }
    var output = sqrt((sqrt((l**2)+(w**2))**2)+(h**2));
    return output;
}
function vertOfPorab(a, b, c){
    if (!isInt(a) && !isInt(b) && !isInt(c)){
        return false;
    }
    var xVrt = (-(b))/(2*(a));
    var yVrt = (a*(xVrt)**2)+(b*(xVrt))+(c);
    return [xVrt, yVrt];
}
function pointOnPorab(x, a, b, c){
    if (!isInt(a) && !isInt(b) && !isInt(c) && !isInt(x)){
        return false;
    }
    c = c-x;
    var topPlus = -(b)+sqrt(b**2 - (4*(a)*(c)));
    var botPlus = (2*(a));
    var topMins = -(b)-sqrt(b**2 - 4*(a)*(c));
    var botMins = (2*(a));
    return [[(topPlus/botPlus), x], [(topMins/botMins), -x]];
}