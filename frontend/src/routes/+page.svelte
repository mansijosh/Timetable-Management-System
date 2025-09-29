<script lang="ts">
  import { goto } from "$app/navigation";
  import { writable } from "svelte/store";

  // --- Common state ---
  const showLogin = writable(false); // false = show register by default

  // Login stores
  const loginUsername = writable("");
  const loginPassword = writable("");
  const loginError = writable("");

  // Register stores
  const regUsername = writable("");
  const regEmail = writable("");
  const regPassword = writable("");
  const regError = writable("");
  const regSuccess = writable("");

  // --- Login Function ---
  async function loginUser() {
    loginError.set("");
    const formData = new URLSearchParams();
    formData.append("username", $loginUsername);
    formData.append("password", $loginPassword);

    try {
      const res = await fetch("http://localhost:8000/auth/login", {
        method: "POST",
        headers: { "Content-Type": "application/x-www-form-urlencoded" },
        body: formData
      });

      if (!res.ok) {
        const data = await res.json();
        loginError.set(data.detail || "Login failed");
        return;
      }

      const data = await res.json();
      localStorage.setItem("token", data.access_token);
      goto("/dashboard");
    } catch (err: unknown) {
      if (err instanceof Error) loginError.set(err.message);
      else loginError.set(String(err));
    }
  }

  // --- Register Function ---
  async function registerUser() {
    regError.set("");
    regSuccess.set("");

    const user = {
      username: $regUsername,
      email: $regEmail,
      password: $regPassword
    };

    try {
      const res = await fetch("http://localhost:8000/auth/register", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(user)
      });

      if (!res.ok) {
        const data = await res.json();
        regError.set(data.detail || "Registration failed");
        return;
      }

      regSuccess.set("✅ Registration successful! You can now login.");
      // Clear fields
      regUsername.set("");
      regEmail.set("");
      regPassword.set("");
      showLogin.set(true); // automatically show login after successful registration
    } catch (err: unknown) {
      if (err instanceof Error) regError.set(err.message);
      else regError.set(String(err));
    }
  }

  function toggleForm() {
    showLogin.update(v => !v);
  }
</script>

<div class="min-h-screen flex items-center justify-center bg-gray-100">
  <div class="bg-white p-8 rounded shadow-md w-full max-w-md">
    <h1 class="text-3xl font-bold mb-6 text-center" style="font-family: 'Poppins', sans-serif;">
  Welcome to TimetableIQ
</h1>


    {#if $showLogin}
      <!-- --- LOGIN FORM --- -->
      <h2 class="text-2xl font-semibold mb-4 text-center">Login</h2>

      {#if $loginError}
        <div class="bg-red-100 text-red-700 p-2 mb-4 rounded">{$loginError}</div>
      {/if}

      <input
        type="text"
        placeholder="Username"
        bind:value={$loginUsername}
        class="w-full p-3 mb-4 border rounded focus:outline-none focus:ring-2 focus:ring-blue-400"
      />
      <input
        type="password"
        placeholder="Password"
        bind:value={$loginPassword}
        class="w-full p-3 mb-4 border rounded focus:outline-none focus:ring-2 focus:ring-blue-400"
      />
      <button
        on:click={loginUser}
        class="w-full bg-blue-500 text-white py-3 rounded hover:bg-blue-600 transition-colors mb-2"
      >
        Login
      </button>

      <p class="text-sm text-center text-gray-600 mt-2">
        Don't have an account?
        <span class="text-blue-500 cursor-pointer hover:underline" on:click={toggleForm}>Register here</span>
      </p>

    {:else}
      <!-- --- REGISTER FORM --- -->
      <h2 class="text-2xl font-semibold mb-4 text-center">Register</h2>

      {#if $regError}
        <div class="bg-red-100 text-red-700 p-2 mb-4 rounded">{$regError}</div>
      {/if}
      {#if $regSuccess}
        <div class="bg-green-100 text-green-700 p-2 mb-4 rounded">{$regSuccess}</div>
      {/if}

      <input
        type="text"
        placeholder="Username"
        bind:value={$regUsername}
        class="w-full p-3 mb-4 border rounded focus:outline-none focus:ring-2 focus:ring-green-400"
      />
      <input
        type="email"
        placeholder="Email"
        bind:value={$regEmail}
        class="w-full p-3 mb-4 border rounded focus:outline-none focus:ring-2 focus:ring-green-400"
      />
      <input
        type="password"
        placeholder="Password"
        bind:value={$regPassword}
        class="w-full p-3 mb-4 border rounded focus:outline-none focus:ring-2 focus:ring-green-400"
      />
      <button
        on:click={registerUser}
        class="w-full bg-green-500 text-white py-3 rounded hover:bg-green-600 transition-colors mb-2"
      >
        Register
      </button>

      <p class="text-sm text-center text-gray-600 mt-2">
        Already have an account?
        <span class="text-blue-500 cursor-pointer hover:underline" on:click={toggleForm}>Login here</span>
      </p>
    {/if}
  </div>
</div>
