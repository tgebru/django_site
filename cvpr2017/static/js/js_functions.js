  $( document ).ready(function() {
    //show streetview image
    var canvas = document.getElementById('img_div');
    var context = canvas.getContext('2d');
    var img = new Image;
    img.onload = function() {
        var bbox_x1 = {{ bbox.pleft }} * ({{ image.oriwidth }} / {{ bbox.width }});
        var bbox_width = ({{ bbox.pright }} - {{ bbox.pleft }} + 1) * ({{ image.oriwidth }} / {{ bbox.width }});
        var bbox_y1 = {{ bbox.ptop }} * ({{ image.oriheight }}/{{ bbox.height }});
        var bbox_height = ({{ bbox.pbottom }} - {{ bbox.ptop }} + 1) * ({{ image.oriheight }} / {{ bbox.height }});
        
        var sourceX= Math.max(0,bbox_x1-10);
        var sourceY= Math.max(0,bbox_y1-10);
        var sourceWidth=bbox_width+20;
        var sourceHeight=bbox_height+20;
        var destWidth = sourceWidth;
        var destHeight =sourceHeight;
        //var destX = canvas.width / 2 - destWidth / 2;
        //var destY = canvas.height / 2 - destHeight / 2;
        var destX=10;
        var destY=10;
        //draw bounding box
        context.drawImage(img, sourceX, sourceY, sourceWidth, sourceHeight, destX, destY, destWidth, destHeight);

      }
        img.src = '{{image.url}}';

    //Auto complete combobox
    $(function() {
      var make_names = [];
      $('.make_names').each(function() {
        make_names.push($(this).val());
      });
      $("#makes").autocomplete({
          minLength: 0,
          source: make_names,
       }).on("focus",function (){
          $(this).autocomplete("search","");
       })
       .data( "ui-autocomplete" )._renderItem = function( ul, item ) {
          var make=item.label.split(" ").join('-');
          return $( "<li>" )
          .append( '<a href="/streetview/'+make+'">'+item.label+"</a>" )
          .appendTo( ul );
        };
 
   $(function() {
      $( "#menu" ).menu();
   });
    $('.button').button();
  });
})
