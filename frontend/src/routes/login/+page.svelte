<script lang="ts">
    import { goto } from "$app/navigation";
    import { writable } from "svelte/store";
  
    const username = writable("");
    const password = writable("");
    const error = writable("");
  
    async function loginUser() {
      error.set("");
      const user = { username: $username, password: $password };
  
      try {
        const res = await fetch("http://localhost:8000/auth/login", {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify(user)
        });
  
        if (!res.ok) {
  const data = await res.json();
  error.set(data.detail || JSON.stringify(data) || "Login failed");
  return;
}
  
        const data = await res.json();
        localStorage.setItem("token", data.access_token);
        goto("/dashboard"); // redirect after login
      } catch (err: unknown) {
        if (err instanceof Error) error.set(err.message);
        else error.set(String(err));
      }
    }
  </script>
  
  <div class="min-h-screen flex items-center justify-center bg-gray-100">
    <div class="bg-white p-8 rounded shadow-md w-full max-w-md">
      <h1 class="text-2xl font-bold mb-6 text-center">Login</h1>
  
      {#if $error}
        <div class="bg-red-100 text-red-700 p-2 mb-4 rounded">{$error}</div>
      {/if}
  
      <input
        type="text"
        placeholder="Username"
        bind:value={$username}
        class="w-full p-3 mb-4 border rounded focus:outline-none focus:ring-2 focus:ring-blue-400"
      />
      <input
        type="password"
        placeholder="Password"
        bind:value={$password}
        class="w-full p-3 mb-4 border rounded focus:outline-none focus:ring-2 focus:ring-blue-400"
      />
      <button
        on:click={loginUser}
        class="w-full bg-blue-500 text-white py-3 rounded hover:bg-blue-600 transition-colors"
      >
        Login
      </button>
    </div>
  </div>
  