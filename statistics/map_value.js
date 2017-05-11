function(doc) {
    var doctime=new Date(doc.time);
    var docminute=doctime.getMinutes();
    var docsecond=doctime.getSeconds();
    var currenttime=new Date();
    var currentminute=currenttime.getMinutes();
    var currentsecond=currenttime.getSeconds();
    if(currentminute>docminute){
        var diff=(currentminute-docminute)*60+(currentsecond-docsecond);
}
    if(currentminute==docminute){
        var diff=currentsecond-docsecond;
}
 
    if(diff<-10)
        emit({"coordinate":doc.location,"score":doc.score},diff);
}
//map twitter value within 5 seconds