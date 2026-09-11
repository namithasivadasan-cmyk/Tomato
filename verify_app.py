with open('index3.html', 'r', encoding='utf-8') as f:
    text = f.read()

assert 'id="wheelCanvas"' in text, 'Missing wheelCanvas'
assert 'id="arcadeCanvas"' in text, 'Missing arcadeCanvas'
assert 'id="scratchCanvas"' in text, 'Missing scratchCanvas'
assert 'switchDeliveryMode' in text, 'Missing switchDeliveryMode'
assert 'trainNoSelect' in text, 'Missing trainNoSelect'
assert 'theaterNameSelect' in text, 'Missing theaterNameSelect'
assert 'cartoon_goat_delivery.jpg' in text, 'Missing cartoon_goat_delivery'
assert 'cartoon_goat_meme.jpg' in text, 'Missing cartoon_goat_meme'
assert 'goat_scream.wav' in text, 'Missing goat_scream.wav'
assert 'playRealGoatSound' in text, 'Missing playRealGoatSound'
assert 'playCartoonBleat' in text, 'Missing playCartoonBleat'
assert 'playGoatLaugh' in text, 'Missing playGoatLaugh'
assert 'playCrunchSound' in text, 'Missing playCrunchSound'
print('All HTML & JS assertions passed successfully!')
