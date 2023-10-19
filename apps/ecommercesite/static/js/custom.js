


  
var availableTags = [];
$("#searcproductId").val('');
$.ajax({
  url: '/categorylistAjax',
  type: 'GET',
  async: false,
  success: function (data) {
    
    startAutoComplete(data);
  }
    
});
  function startAutoComplete(availableTags) {
    $("#searchproducts").autocomplete({
      source: availableTags ,
      select: function( event, ui ) {
        // print(ui.item.label )
        // print(ui.item.value )
        // print(ui.item.desc )
        $("#searchproducts").val(ui.item.label);
        $("#searcproductId").val(ui.item.value);
        
        
        
        return false;
     }
    });
}
  
  
    $("#price-range").slider({
      step: 100,
      range: true, 
      min: 0, 
      max: 5000, 
      values: [0, 5000], 
      slide: function(event, ui)
      {$("#priceRange").val(ui.values[0] + " - " + ui.values[1]);}
    });
    $("#priceRange").val($("#price-range").slider("values", 0) + " - " + $("#price-range").slider("values", 1));
    
  