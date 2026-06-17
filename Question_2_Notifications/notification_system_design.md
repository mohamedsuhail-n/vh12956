# Stage 1
- Endpoint: GET /api/v1/notifications
- Endpoint: PATCH /api/v1/notifications/:id/read

# Stage 2
Schema: 
- Students (id, email, name)
- Notifications (id, type, message)
- StudentNotifications (student_id, notification_id, is_read)

# Stage 3
- Query is slow because of full table scan.
- Solution: Add composite index on (student_id, is_read).

# Stage 4
- Solution: Use Redis for caching and cursor-based pagination.

# Stage 5
- Problem: Sequential blocking calls.
- Solution: Use a message broker to process emails and DB writes asynchronously.

# Stage 6
- Algorithm: Filter by category weight (Placement > Result > Event) and sort by timestamp.