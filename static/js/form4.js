$(document).ready(function(){
    $('#file').change(function(e){
        var fileName = e.target.files[0].name;
        var file = e.target.files[0];
	    var img = new Image();

	    img.onload = function() {
	        var sizes = {
	            width:this.width,
	            height: this.height
	        };
	        URL.revokeObjectURL(this.src);

	        console.log('onload: sizes', sizes);
	        console.log('onload: this', this);
            $('#size').text("Width: " + sizes.width  +" px\nHeight: " + sizes.height + " px");

	    }	
        var objectURL = URL.createObjectURL(file);
        img.src = objectURL;	
        $('#file_label').text(fileName);
    });
    $('#upload_mask').change(function(e){
        var fileName2 = e.target.files[0].name;
        $('#file2_label').text(""+fileName2);
    });
    $('select').change(function(e){
        $('#file_label').text(" Image");
        $('#file2_label').text(" Mask");
        $('#size').text("");

	          var upload_mask=document.getElementById('upload_mask');
	          var upload2_div=document.getElementById('upload2_div');
	          var upload1_div=document.getElementById('upload1_div');
	          var reduction_div=document.getElementById('reduction_div');
	          var file=document.getElementById('file');
	          var file2=document.getElementById('file2');
	          var x_red=document.getElementById('x_red_elem');
	          var y_red=document.getElementById('y_red_elem');

	          if(this.selectedIndex == 0){
	            reduction_div.style.display = 'inline';
	            upload1_div.style.display = 'inline';
	            upload2_div.style.display = 'none';

	            file.setAttribute('required','');
	            upload_mask.removeAttribute('required','');
	            x_red.setAttribute('required','');
	            y_red.setAttribute('required','');
	          }
	          else if(this.selectedIndex == 1){
	            reduction_div.style.display = 'none';
	            upload1_div.style.display = 'inline';
	            upload2_div.style.display = 'inline';

	            upload_mask.setAttribute('required','');
	            file.setAttribute('required','');
	            x_red.removeAttribute('required','');
	            y_red.removeAttribute('required','');
	          }
	          else if(this.selectedIndex == 2){
	            reduction_div.style.display = 'inline';
	            upload1_div.style.display = 'inline';
	            upload2_div.style.display = 'inline';

	            file.setAttribute('required','');
	            upload_mask.setAttribute('required','');
	            x_red.setAttribute('required','');
	            y_red.setAttribute('required','');
	          }

    });
});