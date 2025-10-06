<script lang="ts">
  import { goto } from "$app/navigation";

  const menuItems = [
    { name: "Classroom", path: "../classroom", icon: "📚" },
    { name: "Departments", path: "../department", icon: "🏢" },
    { name: "Users", path: "/user", icon: "👥" },
    { name: "Faculty", path: "/faculty", icon: "🧑‍🏫" },
    { name: "Timetable", path: "/timetable", icon: "📅" },
  ];

  function navigate(path: string) {
    goto(path);
  }
</script>

<div class="flex min-h-screen">
  <!-- Sidebar -->
  <aside
    class="w-64 flex flex-col p-6 text-white"
    style="background: linear-gradient(to bottom, #6A89A7, #c7d9ffff);"
  >
    <!-- Admin Panel Title -->
    <h1 class="text-3xl font-bold mb-8 text-center text-yellow-300 drop-shadow-lg">Admin Panel</h1>

    {#each menuItems as item}
      <button
        class="flex items-center gap-4 px-4 py-3 mb-3 rounded-lg transition-all duration-300
               hover:bg-white hover:text-blue-700 shadow-md font-medium text-gray-100"
        on:click={() => navigate(item.path)}
      >
        <span class="text-xl">{item.icon}</span>
        <span>{item.name}</span>
      </button>
    {/each}
  </aside>

  <!-- Main content with background -->
  <main
    class="flex-1 p-8"
    style="background-image: url('/dashboard-bg.jpg'); background-size: cover; background-position: center; min-height: 100vh;"
  >
    <div class="bg-white bg-opacity-80 p-6 rounded-xl shadow-lg min-h-full">
      <slot></slot>
    </div>
  </main>
</div>
