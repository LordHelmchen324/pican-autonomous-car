document.addEventListener('keydown', function(e) {
    if (e.key == 'w') {
        document.getElementById('keytext').innerHTML = 'Up'
    } else if (e.key == 's') {
        document.getElementById('keytext').innerHTML = 'Down'
    } else if (e.key == 'a') {
        document.getElementById('keytext').innerHTML = 'Left'
    } else if (e.key == 'd') {
        document.getElementById('keytext').innerHTML = 'Right'
    }
})

document.addEventListener('keyup', function(e) {
    if (['w', 'a', 's', 'd'].includes(e.key)) {
        document.getElementById('keytext').innerHTML = 'None'
    }
})
