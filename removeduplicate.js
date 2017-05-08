//map
function(doc) {
  emit({"id":doc.id,"content":doc.content,"time":doc.time,"coordinate":doc.location,"score":doc.score},null)
}
//reduce
function(key,value){
  return null;
}