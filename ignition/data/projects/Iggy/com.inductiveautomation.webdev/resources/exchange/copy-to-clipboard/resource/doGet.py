def doGet(request, session):
	toCopy = "'{}'".format(request['params'].get('toCopy', ''))
	
	html = """ 
		<!DOCTYPE html>
		<html style="margin: 0;height: 100%;">
			<head>
				<style>
					.material-symbols-outlined {
						color: #dde1e6;
						font-size: 36px;
						text-align: left;
						font-variation-settings:
							'FILL' 0;
							'wght' 400;
							'GRAD' 0;
							'opsz' 40;
					}
				</style>
				<link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet">
				<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:opsz,wght,FILL,GRAD@20..48,100..700,0..1,-50..200">
			</head>
					
			<body style="display: flex;flex-direction: column;justify-content: center;align-items: center;align-content: center;margin: 0;height: 100%; overflow: hidden">
		
				<span id="copier" class="material-symbols-outlined" style="align-items: center;display: flex; cursor: pointer">content_copy</span>
				<script>
					var copyButton = document.getElementById("copier");
					copyButton.addEventListener('click', function(event) {
						var copyText = document.createElement('textarea');
						copyText.value = """ + toCopy + """
						
						document.body.appendChild(copyText);
						copyText.select();
						
						try {
							var isSuccess = document.execCommand('copy');
							var msg = isSuccess ? "Copy success" : "Copy fail";
							var color_change = isSuccess ? copyButton.style.color = "#03ad00" : copyButton.style.color = "#808080"
							
							setTimeout(function () {
								copyButton.style.color = "#808080";
							}, 3000);
							
							console.log(msg);
						} catch(err) {
							console.log("Something went wrong.");
						};
						document.body.removeChild(copyText);
					});
				</script>
					
			</body>
		</html>
		"""
	return {'html': html}
	