<script lang="ts">
    import { onMount } from "svelte";
    import { goto } from "$app/navigation";
  
    let username = "";
  
    function parseJwt(token: string) {
      try {
        const base64Payload = token.split(".")[1];
        const payload = atob(base64Payload);
        return JSON.parse(payload);
      } catch {
        return null;
      }
    }
  
    onMount(() => {
      const token = localStorage.getItem("token");
      if (!token) {
        goto("/"); // redirect to root (login/register page) if no token
        return;
      }
  
      const data = parseJwt(token);
      if (data?.sub) {
        username = data.sub; // set username from token
      }
    });
  </script>
  
  
  <div class="min-h-screen flex items-center justify-center bg-green-100">
    <h1 class="text-3xl font-bold">Welcome, {username}!</h1>
  </div>
  
  