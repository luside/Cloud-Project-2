//Author:Side Lu<sidel@student.unimelb.edu.au>
//Date: 10/5/2017
//Project:COMP90024 Cluster and Cloud Computing Assignment2
//map
function(doc) {
  emit({"id":doc.id,"content":doc.content,"time":doc.time,"coordinate":doc.location,"score":doc.score},null)
}
//reduce
function(key,value){
  return null;
}
