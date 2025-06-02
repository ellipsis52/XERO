<<<<<<< HEAD
import { render, screen } from '@testing-library/react';
import App from './App';

test('renders learn react link', () => {
  render(<App />);
  const linkElement = screen.getByText(/learn react/i);
  expect(linkElement).toBeInTheDocument();
=======
import React from 'react';
import { render } from "@testing-library/react";
import App from './App';

it('renders without crashing', () => {
  render(<App />);
>>>>>>> 34d1dd5 (Added React integration to Hyperspace)
});
