function blur_switch()
{
    if (document.getElementByID('toggle').checked)
        document.getElementsByName('video').className = 'card-body blur';
    else
        document.getElementsByName('video').className = 'card-body';
}