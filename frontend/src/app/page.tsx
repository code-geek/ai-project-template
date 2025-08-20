export default function HomePage() {
	return (
		<div className="min-h-screen flex items-center justify-center bg-gray-50">
			<div className="text-center">
				<h1 className="text-4xl font-bold text-gray-900 mb-4">
					AI Project Template
				</h1>
				<p className="text-lg text-gray-600 mb-8">
					Django + Next.js Full Stack Application
				</p>
				<div className="space-x-4">
					<a
						href="/api/docs"
						className="inline-block px-6 py-3 bg-blue-600 text-white rounded-lg hover:bg-blue-700"
					>
						API Documentation
					</a>
					<a
						href="http://localhost:8000/api/docs"
						className="inline-block px-6 py-3 bg-gray-600 text-white rounded-lg hover:bg-gray-700"
					>
						Backend API
					</a>
				</div>
			</div>
		</div>
	);
}
