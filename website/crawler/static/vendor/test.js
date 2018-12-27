function blur_switch()
{
    if (document.getElementById('switch').checked)
        for (let index = 0; index < document.getElementsByName('video').length; index++) {
            const element = document.getElementsByName('video')[index];
            element.className = 'card-body blur';
        }
    else
        for (let index = 0; index < document.getElementsByName('video').length; index++) {
            const element = document.getElementsByName('video')[index];
            element.className = 'card-body';
        }
    }

