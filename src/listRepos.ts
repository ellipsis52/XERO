import { tool } from "ai";
import { z } from 'zod';
import { openai } from "@ai-sdk/openai";
import { Octokit } from "@octokit/rest";
import { auth0 } from "@/lib/auth0";

export const listRepos = tool({
  description: 'List respositories for the current user on GitHub',
  parameters: z.object({}),
  execute: async () => {
    const { accessToken } = await auth0.getAccessTokenForConnection({ connection: "github" });
    const octokit = new Octokit({ auth: accessToken });

    const response = await octokit.request('GET /user/repos', {
      visibility: 'all',
    });

    const filteredRepos = response.data.map(repo => ({
      id: repo.id,
      full_name: repo.full_name,
      private: repo.private,
      owner_name: repo.owner.login,
      url: repo.html_url,
      description: repo.description,
      stars: repo.stargazers_count,
      forks: repo.forks_count,
    }));

    return filteredRepos;
  }
});