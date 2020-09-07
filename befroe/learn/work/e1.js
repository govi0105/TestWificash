var keys = Object.keys(request.data).sort();
var result = "";
for(var p=0; p<keys.length; p++){
    if(p>0){
        result += "|";
    }
    result += (keys[p]+"="+request.data[keys[p]]);
}
var token = request.headers.token?request.headers.token:"";
//var mydata = JSON.stringify(request.headers.);
var app_key='oQIhAP24Kb3Bsf7IE14wpl751bQc9VAPsFZ+LdB4riBgg2TDAiEAsSomOO1v8mK2VWhEQh6mttgN';
print(CryptoJS.MD5(app_key+token+result).toString());
//
// var arr = ["a", "b", "c"];
// alert(Object.keys(arr)); // 弹出"0,1,2"



