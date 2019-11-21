document.addEventListener('keydown', function(e) {
    if (e.key == 'w') $('#keytext').text('Up')
    else if (e.key == 's') $('#keytext').text('Down')
    else if (e.key == 'a') $('#keytext').text('Left')
    else if (e.key == 'd') $('#keytext').text('Right')

    if (['w', 'a', 's', 'd'].includes(e.key)) $.post('keydown/' + e.key)
})

document.addEventListener('keyup', function(e) {
    if (['w', 'a', 's', 'd'].includes(e.key)) $('#keytext').text('None')

    if (['w', 'a', 's', 'd'].includes(e.key)) $.post('keyup/' + e.key)
})
