"use client";

import { useChat } from "@ai-sdk/react";
import { useInterruptions } from "@auth0/ai-vercel/react";
import { FederatedConnectionInterrupt } from "@auth0/ai/interrupts";
import { EnsureAPIAccessPopup } from "@/components/auth0-ai/FederatedConnections/popup";

export default function Chat() {
  const { messages, handleSubmit, input, setInput, toolInterrupt } =
    useInterruptions((handler) =>
      useChat({
        onError: handler((error) => console.error("Chat error:", error)),
      })
    );

  return (
    <div>
      {messages.map((message) => (
        <div key={message.id}>
          {message.role === "user" ? "User: " : "AI: "}
          {message.content}
        </div>
      ))}

      {FederatedConnectionInterrupt.isInterrupt(toolInterrupt) && (
        <EnsureAPIAccessPopup
          interrupt={toolInterrupt}
          connectWidget={{
            title: "List Slack channels",
            description:"description ...",
            action: { label: "Check" },
          }}
        />
      )}

      <form onSubmit={handleSubmit}>
        <input value={input} placeholder="Say something..." onChange={(e) => setInput(e.target.value)} />
      </form>
    </div>
  );
}