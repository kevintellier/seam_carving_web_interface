var fileInput = document.querySelector('#file');
    fileInput.addEventListener('change', function() {

        var reader = new FileReader();

        if(reader.readyState == 2){
            	alert('OK1')
            }
        reader.addEventListener('done', function() {
            if(reader.readyState == 2){
            	alert('OK')
            }
        });

        reader.readAsText(fileInput.files[0]);

 	});