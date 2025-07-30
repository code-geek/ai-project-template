import { expect, test } from "@playwright/test";

test.describe("Homepage", () => {
	test("should load successfully", async ({ page }) => {
		await page.goto("/");

		// Check page title
		await expect(page).toHaveTitle(/AI Project Template/);

		// Check main heading is visible
		const heading = page.getByRole("heading", { level: 1 });
		await expect(heading).toBeVisible();
	});

	test("should navigate to login page", async ({ page }) => {
		await page.goto("/");

		// Click login link
		await page.getByRole("link", { name: /login/i }).click();

		// Should be on login page
		await expect(page).toHaveURL("/login");

		// Login form should be visible
		await expect(page.getByRole("button", { name: /sign in/i })).toBeVisible();
	});
});

test.describe("Authentication Flow", () => {
	test("should login successfully", async ({ page }) => {
		await page.goto("/login");

		// Fill login form
		await page.getByLabel("Email").fill("test@example.com");
		await page.getByLabel("Password").fill("testpass123");

		// Submit form
		await page.getByRole("button", { name: /sign in/i }).click();

		// Should redirect to dashboard
		await expect(page).toHaveURL("/dashboard");

		// User menu should be visible
		await expect(page.getByTestId("user-menu")).toBeVisible();
	});

	test("should show validation errors", async ({ page }) => {
		await page.goto("/login");

		// Submit empty form
		await page.getByRole("button", { name: /sign in/i }).click();

		// Should show validation errors
		await expect(page.getByText("Email is required")).toBeVisible();
		await expect(page.getByText("Password is required")).toBeVisible();
	});

	test("should logout successfully", async ({ page }) => {
		// Login first
		await page.goto("/login");
		await page.getByLabel("Email").fill("test@example.com");
		await page.getByLabel("Password").fill("testpass123");
		await page.getByRole("button", { name: /sign in/i }).click();

		// Wait for redirect
		await page.waitForURL("/dashboard");

		// Open user menu and logout
		await page.getByTestId("user-menu").click();
		await page.getByRole("button", { name: /logout/i }).click();

		// Should redirect to homepage
		await expect(page).toHaveURL("/");
		await expect(page.getByRole("link", { name: /login/i })).toBeVisible();
	});
});

test.describe("API Integration", () => {
	test("should fetch and display data", async ({ page }) => {
		await page.goto("/dashboard");

		// Wait for data to load
		await page.waitForSelector('[data-testid="data-list"]');

		// Should display items
		const items = page.locator('[data-testid="data-item"]');
		await expect(items).toHaveCount(10); // Assuming pagination of 10
	});

	test("should handle API errors gracefully", async ({ page }) => {
		// Mock API error
		await page.route("**/api/items", (route) => {
			route.fulfill({
				status: 500,
				contentType: "application/json",
				body: JSON.stringify({ error: "Internal Server Error" }),
			});
		});

		await page.goto("/dashboard");

		// Should show error message
		await expect(page.getByText(/Something went wrong/i)).toBeVisible();
		await expect(
			page.getByRole("button", { name: /try again/i }),
		).toBeVisible();
	});
});
