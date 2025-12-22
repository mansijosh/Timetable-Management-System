<script lang="ts">
  import type { PageData } from './$types';
  import { Trash2 } from 'lucide-svelte';
  import { enhance } from '$app/forms';

  export let data: PageData;
</script>

<div class="min-h-screen bg-gray-100 p-8">
  <div class="mx-auto max-w-6xl">
    <div class="mb-6 rounded-lg bg-white p-6 shadow-md">
      <h1 class="mb-2 text-3xl font-bold">Subjects</h1>
      <p class="text-gray-600">Manage all subjects</p>
    </div>

    <div class="rounded-lg bg-white p-6 shadow-md">
      <h2 class="mb-4 text-2xl font-semibold">All Subjects</h2>

      {#if data.subjects && data.subjects.length > 0}
        <div class="overflow-x-auto">
          <table class="min-w-full divide-y divide-gray-200">
            <thead class="bg-gray-50">
              <tr>
                <th class="px-6 py-3 text-left text-xs font-medium uppercase tracking-wider text-gray-500">
                  Name
                </th>
                <th class="px-6 py-3 text-left text-xs font-medium uppercase tracking-wider text-gray-500">
                  Faculty
                </th>
                <th class="px-6 py-3 text-left text-xs font-medium uppercase tracking-wider text-gray-500">
                  Department
                </th>
                <th class="px-6 py-3"></th>
              </tr>
            </thead>
            <tbody class="divide-y divide-gray-200 bg-white">
              {#each data.subjects as subject}
                <tr class="hover:bg-gray-50">
                  <td class="px-6 py-4 text-sm font-medium text-gray-900">{subject.name}</td>
                  <td class="px-6 py-4 text-sm text-gray-700">{subject.faculty?.name || '-'}</td>
                  <td class="px-6 py-4 text-sm text-gray-700">{subject.department?.name || '-'}</td>
                  <td class="px-6 py-4 text-right">
                    <form method="POST" action="?/deleteSubject" use:enhance>
                      <input type="hidden" name="id" value={subject.id} />
                      <button
                        type="submit"
                        class="text-red-600 hover:text-red-800"
                        title="Delete Subject"
                      >
                        <Trash2 class="w-5 h-5 inline-block" />
                      </button>
                    </form>
                  </td>
                </tr>
              {/each}
            </tbody>
          </table>
        </div>
      {:else}
        <div class="py-8 text-center text-gray-500">
          <p>No subjects found.</p>
        </div>
      {/if}
    </div>

    {#if data.error}
      <div class="mt-4 rounded-lg bg-red-100 p-4 text-red-700">
        <p class="font-semibold">Error loading subjects:</p>
        <p>{data.error}</p>
      </div>
    {/if}
  </div>
</div>
