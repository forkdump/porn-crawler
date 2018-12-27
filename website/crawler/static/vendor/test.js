function blur_switch()
{
    document.getElementsByName('video').forEach
    (element => element.className = document.getElementById('switch').checked ? 'card-body blur' : 'card-body')
}