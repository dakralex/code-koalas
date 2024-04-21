attribute vec2 aCRSCoords;
attribute vec2 aExtrudeCoords;
uniform mat4 uTransformMatrix;
uniform vec2 uPixelSize;

varying vec2 vPixel;
varying float vMaxRadius;

attribute float severity;
varying float vSeverity;

void main(void) {
    vMaxRadius = 5.0 - severity;
    vPixel = aExtrudeCoords * 5.0;
    vSeverity = severity;
    gl_Position = uTransformMatrix * vec4(aCRSCoords, 1.0, 1.0) + vec4(aExtrudeCoords * uPixelSize * 5.0, 0.0, 0.0);
}
