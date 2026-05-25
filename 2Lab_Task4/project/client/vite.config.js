import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

export default defineConfig({
  plugins: [react()],
  server: {
    host: true, // слушать все интерфейсы
    port: 5173,
    watch: {
      usePolling: true, // нужно для hot-reload в Docker на Windows/Mac
    },
  },
})
