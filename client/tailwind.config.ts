import type { Config } from "tailwindcss";

const config: Config = {
  content: [
    "./pages/**/*.{js,ts,jsx,tsx,mdx}",
    "./src/components/**/*.{js,ts,jsx,tsx,mdx}",
    "./src/app/**/*.{js,ts,jsx,tsx,mdx}",
  ],
  theme: {
    extend: {
      colors: {
        background: "var(--background)",
        foreground: "var(--foreground)",
        blue: {
          "50": "#ecf9ff",
          "100": "#d4efff",
          "200": "#b2e5ff",
          "300": "#7dd7ff",
          "400": "#40beff",
          "500": "#149cff",
          "600": "#007aff",
          "700": "#0062ff",
          "800": "#0052d6",
          "900": "#0846a0",
          "950": "#0a2b61",
        },
      },
    },
  },
  plugins: [],
};
export default config;
