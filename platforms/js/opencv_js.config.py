# Classes and methods whitelist

core = {
    '': [
        'bitwise_not',
        'perspectiveTransform'
    ]
}

imgproc = {'': [
    'boundingRect',
    'contourArea',
    'cvtColor',
    'dilate',
    'findContours',
    'GaussianBlur',
    'getPerspectiveTransform',
    'morphologyDefaultBorderValue',
    'putText',
    'rectangle',
    'resize',
    'threshold',
    'warpPerspective'
],
}


white_list = makeWhiteList([core, imgproc])
