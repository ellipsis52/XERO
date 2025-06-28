"use client";

import { useUser } from "@auth0/nextjs-auth0";

export default function Page() {
  // Extract the user object and loading state from Auth0.
  const { user, isLoading } = useUser();

  if (isLoading) return <div>Loading...</div>;

  // If no user, show sign-up and login buttons.
  if (!user) {
    return (
      <main className="flex flex-col items-center justify-center h-screen p-10">
        <a href="/auth/login?screen_hint=signup">
          <button>Sign up</button>
        </a>
        <a href="/auth/login">
          <button>Log in</button>
        </a>
      </main>
    );
  }

  // If user exists, show a welcome message and logout button.
  return (
    <main className="flex flex-col items-center justify-center h-screen p-10">
      <h1>Welcome, {user.name}!</h1>
      <p>
        <a href="/auth/logout">
          <button>Log out</button>
        </a>
      </p>
    </main>
  );
}
"use client";

import React from "react";
import { useChat } from "@ai-sdk/react";

export default function ChatPage() {
  const { messages, input, handleInputChange, handleSubmit } = useChat({});
  return (
    <main className="flex flex-col items-center justify-center h-screen p-10">
      <div className="flex flex-col gap-2">
        {messages.map((message) => (
          <div key={message.id}>
            {message.role === "user" ? "User: " : "AI: "}
            {message.content}
          </div>
        ))}
      </div>

      <form onSubmit={handleSubmit}>
        <input
          name="prompt"
          value={input}
          className="w-full border"
          onChange={handleInputChange}
        />
        <button
          className="p-2 m-2 border-2 rounded-md border-zinc-800 bg-zinc-800 text-zinc-50 hover:bg-black"
          type="submit"
        >
          Send
        </button>
      </form>
    </main>
  );
}
// ...

// If no user session, show sign-up and login buttons.
if (!user) {
  return (
    <main className="flex flex-col items-center justify-center h-screen p-10">
      <a href="/auth/login?screen_hint=signup&connection=google-oauth2&access_type=offline&prompt=consent">
        <button>Sign up with Google</button>
      </a>
      <a href="/auth/login?connection=google-oauth2&access_type=offline&prompt=consent">
        <button>Log in with Google</button>
      </a>
    </main>
  );
}
"use client";

import { useUser } from "@auth0/nextjs-auth0";
import { useCompletion } from "@ai-sdk/react";

export default function Page() {
  // Extract the user object and loading state from Auth0.
  const { user, isLoading } = useUser();
  // Use streaming response from the Next.js route.
  const { completion, input, handleInputChange, handleSubmit } = useCompletion({
    api: "/api/chat",
  });

  if (isLoading) return <div>Loading...</div>;
  // If no user, show sign-up and login buttons.
  if (!user) {
    return (
      // ...
    );
  }

  return (
    <main className="flex flex-col items-center justify-center h-screen p-10">
      <h1>Welcome, {user.name}!</h1>
      {/* Main form for interacting with the AI. */}
      <form onSubmit={handleSubmit}>
        <input
          name="prompt"
          value={input}
          onChange={handleInputChange}
          id="input"
          className="p-2 m-2 border-2 rounded-md border-zinc-800"
        />
        <button
          type="submit"
          className="p-2 m-2 border-2 rounded-md border-zinc-800 bg-zinc-800 text-zinc-50 hover:bg-black"
        >
          Submit
        </button>
        <div>{completion}</div>
      </form>
    </main>
  );
}
'use client';

import { useChat } from '@ai-sdk/react';

export default function Chat() {
  const { messages, input, handleInputChange, handleSubmit } = useChat();

  return (
    <div className="flex flex-col w-full max-w-3xl py-24 mx-auto text-gray-100 stretch">
      {messages.map(message => (
        <div key={message.id} className="whitespace-pre-wrap">
          {message.role === 'user' ? 'User: ' : 'AI: '}
          {message.parts.map((part, i) => {
            switch (part.type) {
              case 'text':
                return <div key={`${message.id}-${i}`}>{part.text}</div>;
            }
          })}
        </div>
      ))}

      <form onSubmit={handleSubmit}>
        <input onChange={handleInputChange} value={input} placeholder="Say something..." className="fixed bottom-0 w-full max-w-3xl p-2 mb-8 text-black border rounded shadow-xl border-zinc-300" />
      </form>
    </div>
  );
}
// src/app/page.tsx
import { auth0 } from "@/lib/auth0";

async function generateAccountLinkingHref(requested_connection: string) {
  "use server";
  const session = await auth0.getSession();
  const id_token_hint = session!.tokenSet!.idToken!;
  const authParams = new URLSearchParams({
    scope: "link_account openid profile offline_access",
    requested_connection,
    id_token_hint,
  }).toString();

  return `/auth/login?${authParams}`;
}

export default async function Home() {
  return (
    <a href={await generateAccountLinkingHref("google-oauth2")}>
      Link Google Account
    </a>
  );
}