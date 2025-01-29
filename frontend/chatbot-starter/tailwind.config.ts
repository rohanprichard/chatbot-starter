import type { Config } from "tailwindcss";

export default {
    darkMode: ["class"],
    content: [
    "./src/**/*.{js,ts,jsx,tsx,mdx}",
  ],
  theme: {
  	extend: {
  		colors: {
  			background: 'hsl(var(--background))',
  			foreground: 'hsl(var(--foreground))',
  			card: {
  				DEFAULT: 'hsl(var(--background))',
  				foreground: 'hsl(var(--foreground))'
  			},
  			popover: {
  				DEFAULT: 'hsl(var(--background))',
  				foreground: 'hsl(var(--foreground))'
  			},
  			primary: {
  				DEFAULT: 'hsl(var(--foreground))',
  				foreground: 'hsl(var(--background))'
  			},
  			secondary: {
  				DEFAULT: 'hsl(var(--background))',
  				foreground: 'hsl(var(--foreground))'
  			},
  			muted: {
  				DEFAULT: 'hsl(var(--background))',
  				foreground: 'hsl(var(--foreground))'
  			},
  			accent: {
  				DEFAULT: 'hsl(var(--background))',
  				foreground: 'hsl(var(--foreground))'
  			},
  			destructive: {
  				DEFAULT: 'hsl(var(--background))',
  				foreground: 'hsl(var(--foreground))'
  			},
  			border: 'hsl(var(--border))',
  			input: 'hsl(var(--background))',
  			ring: 'hsl(var(--foreground))',
  			turquoise: {
  				light: 'hsl(var(--turquoise-light))',
  				DEFAULT: 'hsl(var(--turquoise))',
  				dark: 'hsl(var(--turquoise-dark))',
  			},
  			lavender: {
  				light: 'hsl(var(--lavender-light))',
  				DEFAULT: 'hsl(var(--lavender))',
  				dark: 'hsl(var(--lavender-dark))',
  			},
  			yellow: {
  				light: 'hsl(var(--yellow-light))',
  				DEFAULT: 'hsl(var(--yellow))',
  				dark: 'hsl(var(--yellow-dark))',
  			}
  		},
  		borderRadius: {
  			lg: 'var(--radius)',
  			md: 'calc(var(--radius) - 2px)',
  			sm: 'calc(var(--radius) - 4px)'
  		}
  	}
  },
  plugins: [require("tailwindcss-animate")],
} satisfies Config;
