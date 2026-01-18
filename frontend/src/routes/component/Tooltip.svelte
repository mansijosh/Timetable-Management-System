<script lang="ts">
  import { buttonVariants } from "$lib/components/ui/button";
  import * as Tooltip from "$lib/components/ui/tooltip";

  export let description: string;
</script>

<Tooltip.Provider>
  <Tooltip.Root>
    <Tooltip.Trigger class={buttonVariants({ variant: "outline" })}>
      <slot name="trigger" />
    </Tooltip.Trigger>

    <Tooltip.Content>
      <p>{description}</p>
    </Tooltip.Content>
  </Tooltip.Root>
</Tooltip.Provider>
