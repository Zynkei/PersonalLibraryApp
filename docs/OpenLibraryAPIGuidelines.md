# Usage Guidelines
Open Library’s APIs exist to support the open book ecosystem and human-centered discovery. Due to limited resources, they are not intended to serve as a data backend for third-party services.

We prioritize:
- Open-source and mission-aligned projects
- Library and education tools
- Human-facing discovery and lookup services
- Real-time, low-volume, high-value use

These APIs are not intended to serve as a bulk data backend or high-traffic commercial infrastructure. For bulk access, please download our free monthly data dumps or contact us at openlibrary@archive.org.

## Please Do:
- Make useful, time-sensitive requests on behalf of human users
- Cache responses whenever possible
- Identify your application with a User-Agent header and email

## Please Do Not:
- Scrape HTML pages (use API endpoints instead)
- Distribute traffic across 5+ IPs
- Harvest data in bulk
- Make hundreds of single-book requests (use search.json for batch results)
- Use Open Library as a backend for high-traffic services

Violations may result in aggressive rate limiting or blocking.

# Rate Limits
If your application will make regular, frequent use of Open Library's APIs (e.g. multiple calls per minute), please add a HEADER that specifies a User-Agent string with (a) the name of your application and (b) your contact email or phone number, so we may contact you when we notice high request volume. In addition, identified requests will enjoy a 3x request limit.

Default (non-identified requests):
- 1 request per second

Identified requests (with User-Agent and email):
- 3 requests per second

User-Agent: MyLibraryApp (contact@example.org)