 
<script lang="ts">
     import { Button } from "$lib/components/ui/button/index.js";
     import * as AlertDialog from "$lib/components/ui/alert-dialog/index.js";
    let message = "Hello Department";
  </script>
  
  <div class="flex items-center justify-center min-h-screen bg-gray-100">
    <div class="flex flex-col items-center space-y-4">
        <h1 class="text-3xl font-bold">{message}</h1>
    
   
    
        <AlertDialog.Root>
            <AlertDialog.Trigger>Open</AlertDialog.Trigger>
            <AlertDialog.Content>
              <AlertDialog.Header>
                <AlertDialog.Title>Are you absolutely sure?</AlertDialog.Title>
                <AlertDialog.Description>
                  This action cannot be undone. This will permanently delete your account
                  and remove your data from our servers.
                </AlertDialog.Description>
              </AlertDialog.Header>
              <AlertDialog.Footer>
                <AlertDialog.Cancel>Cancel</AlertDialog.Cancel>
                <AlertDialog.Action>Continue</AlertDialog.Action>
              </AlertDialog.Footer>
            </AlertDialog.Content>
          </AlertDialog.Root>
        </div>
  </div>
 