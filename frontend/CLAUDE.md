# Frontend AI Instructions

## 🏗️ Frontend Architecture

- **Framework**: Next.js 15 with App Router
- **Language**: TypeScript (strict mode)
- **Styling**: Tailwind CSS + shadcn/ui
- **State**: Zustand for global state
- **API Client**: Native fetch with typed wrappers

## 📁 Project Structure

```plaintext
src/
├── app/              # Next.js App Router
│   ├── layout.tsx   # Root layout
│   ├── page.tsx     # Home page
│   └── (auth)/      # Auth group
├── components/
│   ├── ui/          # shadcn/ui components
│   └── features/    # Feature components
├── lib/
│   ├── api.ts       # API client
│   └── utils.ts     # Utilities
└── types/           # TypeScript types
```

## 📝 Component Patterns

### Server Components (default)

```tsx
// app/products/page.tsx
export default async function ProductsPage() {
  const products = await getProducts()

  return (
    <div>
      {products.map(product => (
        <ProductCard key={product.id} product={product} />
      ))}
    </div>
  )
}
```

### Client Components

```tsx
'use client'

import { useState } from 'react'

export function Counter() {
  const [count, setCount] = useState(0)

  return (
    <button onClick={() => setCount(count + 1)}>
      Count: {count}
    </button>
  )
}
```

## 🎨 UI Components

### Adding shadcn/ui components

```bash
npx shadcn@latest add button
npx shadcn@latest add form
npx shadcn@latest add dialog
```

### Component usage

```tsx
import { Button } from '@/components/ui/button'
import { Dialog } from '@/components/ui/dialog'

export function MyComponent() {
  return (
    <Button variant="outline" size="sm">
      Click me
    </Button>
  )
}
```

## 🔧 Common Tasks

### Create new page

```bash
# Create directory and page
mkdir -p src/app/products
touch src/app/products/page.tsx
```

### API Integration

```typescript
// lib/api.ts
const API_BASE = process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8000/api'

export async function getProducts() {
  const res = await fetch(`${API_BASE}/products/`)
  if (!res.ok) throw new Error('Failed to fetch')
  return res.json()
}
```

### State Management

```typescript
// stores/auth.ts
import { create } from 'zustand'

interface AuthState {
  user: User | null
  login: (user: User) => void
  logout: () => void
}

export const useAuthStore = create<AuthState>((set) => ({
  user: null,
  login: (user) => set({ user }),
  logout: () => set({ user: null }),
}))
```

## 🧪 Testing

```bash
# Run E2E tests
npm run test:e2e

# Run with UI
npm run test:e2e:ui
```

## 🛡️ Best Practices

- Use Server Components by default
- Add 'use client' only when needed
- Keep components small and focused
- Use TypeScript strictly
- Follow Tailwind CSS conventions
- Test critical user flows with Playwright
