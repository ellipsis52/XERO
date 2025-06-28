/app/api/chat/route.js

import { openai } from "@ai-sdk/openai"
import { streamText, tool } from "ai"
import { z } from 'zod';
import { auth0 } from "@/lib/auth0";

export const maxDuration = 60;

export async function POST(req) {
  const { messages } = await req.json()

  const system = `You're a helpful AI agent that helps analyze salesforce data`

  const response = streamText({
    model: openai('gpt-4o'),
    messages,
    system,
    maxSteps: 10,
    tools: {
      listOpportunities: tool({ // salesforce tool call to get a list of opportunities
        description: 'Get a list of opportunities from Salesforce',
        parameters: z.object({
          limit: z.number().default(10).describe('The maximum number of opportunities to return'),
        }),
        execute: async ({ limit }) => {
          const instanceUrl = process.env.SALESFORCE_INSTANCE_URL;

          const endpoint = `query/?q=${encodeURIComponent(`SELECT Id, Name, StageName, CloseDate FROM Opportunity LIMIT ${limit}`)}`;
          const url = `${instanceUrl}/services/data/v57.0/${endpoint}`;

          // call auth0 to get the access token
          const { accessToken } = await (auth0.getAccessTokenForConnection({ connection: "sfdc" }));

          const response = await fetch(url, {
            method: "GET",
            headers: {
              'Authorization': `Bearer ${accessToken}`,
              'Content-Type': 'application/json'
            },
          });
          return await response.json();
        },
      }),
    }
  })
  return response.toDataStreamResponse();
}