# sv

Everything you need to build a Svelte project, powered by [`sv`](https://github.com/sveltejs/cli).

## Creating a project

If you're seeing this, you've probably already done this step. Congrats!

```sh
# create a new project in the current directory
npx sv create

# create a new project in my-app
npx sv create my-app
```

## Developing

Once you've created a project and installed dependencies with `npm install` (or `pnpm install` or `yarn`), start a development server:

```sh
npm run dev

# or start the server and open the app in a new browser tab
npm run dev -- --open
```

## Building

To create a production version of your app:

```sh
npm run build
```

You can preview the production build with `npm run preview`.

> To deploy your app, you may need to install an [adapter](https://svelte.dev/docs/kit/adapters) for your target environment.

## Authentication Flow

In this project, **user authentication** has been implemented with the following structure:

### Register
- Takes three input fields:
  - **Username**
  - **Email ID**
  - **Password**

### Login
- Takes two input fields:
  - **Username** → This is actually the **email** entered at the time of registration  
  - **Password** → Same as the password set during registration

> Note: During login, the **email is used as the username** for authentication.

### Using Lucide Icons in Svelte
# Step 1: Install Lucide Svelte
npm install lucide-svelte

# Step 2: Import the Icon in Your Component
  <script>
    import { CalendarDays } from 'lucide-svelte';
  </script>

# Step 3: Use the Icon in Your Template
<CalendarDays class="w-6 h-6 text-black" />


# w-6 h-6 sets the size of the icon.

# text-black sets the color. You can adjust it to any color you want.

