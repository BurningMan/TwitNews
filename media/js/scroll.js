
			tweetId = 1;
            this.count = 0;
            this.mode = 1;
            this.id = 1;
			

function wheel(event)
{    
    var wheelDelta = 0;
    
    if (!event) 
    {
        event = window.event;
    }
    if (event.wheelDelta) 
    {
        // В IE и Opera при сдвиге колеса на один шаг event.wheelDelta принимает значение 120
        // Значения сдвига в этих двух браузерах совпадают по знаку.
        wheelDelta = event.wheelDelta/120;
    } 
    else if (event.detail) 
    {
        // В Mozilla, значение wheelDelta отличается по знаку от значения в IE.
        // Сдвиг колеса на один шаг соответствует значению 3 параметра event.detail          
        wheelDelta = -event.detail/3;
    }
    // При скроллинге вверх wheelDelta > 0
    // При скролинге вниз - wheelDelta < 0
    if (wheelDelta)
    {
        if(wheelDelta > 0){
            up();
        }

        if(wheelDelta < 0){
            down();
        }
    }
   // Убиваем событие (чтобы страница не скроллилась)
    if (event.preventDefault)
    {
        event.preventDefault();
    }
    event.returnValue = false;
    blockEvent(event);
}

function handleOnMouseWheel(event)
{
    wheel(event);
}

    function init()
{
    if (document.getElementById('tweets').addEventListener)
        document.getElementById('tweets').addEventListener('DOMMouseScroll', handleOnMouseWheel, false);
    document.getElementById('tweets').onmousewheel = handleOnMouseWheel;
}

			function delta(progress) {
				return progress;
			}
            

            function down(){
                if(this.mode == 1)
                    moveDown();
            }

            function up(){
                if(this.mode == 1)
                    moveUp();
            }

			function moveDown(){
				if(tweetId < 6){
                    this.mode = 0;
					var element = document.getElementById(tweetId);
					element.style.visibility = 'hidden';
					var from = 0; // Начальная координата X
					var to = -105; // Конечная координата X
					var duration = 100; // Длительность - 1 секунда
					var start = new Date().getTime(); // Время старта

					setTimeout(function() {
						var now = (new Date().getTime()) - start; // Текущее время
						var progress = now / duration; // Прогресс анимации
	
						var result = (to - from) * delta(progress) + from;

						element.style.marginTop = result + "px";

						if (progress < 1) // Если анимация не закончилась, продолжаем
							setTimeout(arguments.callee, 10);
						else{
                            this.count++;
							this.tweetId = this.tweetId + 1;
							element.style.marginTop = 0 + "px";
							element.style.display = 'none';
							element.style.visibility = 'visible';
							var newElement = document.getElementById(tweetId + 4);
							newElement.style.display = 'inline';
                            if (this.count < 5)
                                moveDown();
                            if (this.count == 5){
                                this.count = 0;
                                this.mode = 1;
                            }
						}
					}, 10);
				}
			}
			
			function moveUp(){
				if(tweetId > 1){
                    this.mode = 0;
					var element = document.getElementById(tweetId);
					var oldElement = document.getElementById(tweetId + 4);
					oldElement.style.display = 'none';
					var from = 0; // Начальная координата X
					var to = 105; // Конечная координата X
					var duration = 100; // 
					var start = new Date().getTime(); // Время старта

					setTimeout(function() {
						var now = (new Date().getTime()) - start; // Текущее время
						var progress = now / duration; // Прогресс анимации
	
						var result = (to - from) * delta(progress) + from;

						element.style.marginTop = result + "px";

						if (progress < 1) // Если анимация не закончилась, продолжаем
							setTimeout(arguments.callee, 10);
						else{
                            this.count++;
							this.tweetId = this.tweetId - 1;
							var newElement = document.getElementById(tweetId);
							newElement.style.display = 'inline';
							element.style.marginTop = 0 + "px";
                            if (this.count < 5)
                                moveUp();
                            if (this.count == 5){
                                this.count = 0;
                                this.mode = 1;
                            }
						}
					}, 10);
				}
			}

window.onload = init;

			
function changeID(newId){
    this.id = newId;
}

