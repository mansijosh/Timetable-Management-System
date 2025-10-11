module.exports = {
	root: true,
	parser: '@typescript-eslint/parser',
	parserOptions: {
		sourceType: 'module',
		ecmaVersion: 2020
	},
	plugins: ['svelte3', '@typescript-eslint'],
	overrides: [
		{
			files: ['*.svelte'],
			processor: 'svelte3/svelte3'
		}
	],
	settings: {
		'svelte3/typescript': require('typescript')
	},
	env: {
		browser: true,
		es2021: true
	},
	rules: {
		// optionally add rules or leave empty
	}
};
