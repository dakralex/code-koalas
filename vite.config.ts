import {defineConfig} from 'vite'
import react from '@vitejs/plugin-react'
import glsl from 'vite-plugin-glsl'
import postcssNesting from 'postcss-nesting'
import postcssCustomMedia from 'postcss-custom-media'

// https://vitejs.dev/config/
export default defineConfig({
    base: '',
    build: {
        outDir: 'docs',
    },
    plugins: [react(), glsl()],
    css: {
        postcss: {
            plugins: [
                postcssNesting,
                postcssCustomMedia,
            ]
        }
    }
})
