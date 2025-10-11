import { writable } from 'svelte/store';

export const user = writable<{ name: string; email: string; avatar: string }>({
    name: '',
    email: '',
    avatar: ''
});
