import franken from 'franken-ui/shadcn-ui/preset-quick';

/** @type {import('tailwindcss').Config} */
export default {
	presets: [franken()],
	content: ["./templates/**/*.{html,js}", "./templates/**/**/*.{html,js}"],
	safelist: [
		{
			pattern: /^uk-/
		},
		'ProseMirror',
		'ProseMirror-focused',
		'tiptap'
	],
	theme: {
		extend: {
		  fontFamily: {
			poppins: ['Poppins', 'sans-serif'],
			sakarta: ['Sakarta Plus', 'sans-serif'],
		  },     
		},
	  },
	plugins: []
};
