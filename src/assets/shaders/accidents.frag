precision highp float;
varying vec2 vPixel;
varying float vMaxRadius;
varying float vSeverity;

void main(void) {
    // Radius is now in pixels, not in 0-1.
    float radiusSquared = vPixel.x * vPixel.x + vPixel.y * vPixel.y;

    float innerRadius = vMaxRadius - 2.0;
    float alpha = smoothstep(vMaxRadius*vMaxRadius, innerRadius*innerRadius, radiusSquared);

    if (vSeverity <= 1.0) {
        gl_FragColor = vec4(1.0, 0.149, 0.149, alpha);
    } else if (vSeverity <= 2.0) {
        gl_FragColor = vec4(1.0, 0.675, 0.149, alpha);
    } else {
        gl_FragColor = vec4(0.588, 0.929, 0.141, alpha);
    }
}