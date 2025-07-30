# Production Deployment Checklist

Use this checklist before deploying to production to ensure your application is secure, performant, and reliable.

## 🔒 Security

### Django Security

- [ ] `DEBUG = False` in production settings
- [ ] Strong `SECRET_KEY` (50+ characters, never committed to version control)
- [ ] `ALLOWED_HOSTS` properly configured with your domains
- [ ] HTTPS enforced with `SECURE_SSL_REDIRECT = True`
- [ ] Security headers configured:
  - [ ] `SECURE_HSTS_SECONDS = 31536000`
  - [ ] `SECURE_HSTS_INCLUDE_SUBDOMAINS = True`
  - [ ] `SECURE_HSTS_PRELOAD = True`
  - [ ] `SESSION_COOKIE_SECURE = True`
  - [ ] `CSRF_COOKIE_SECURE = True`
  - [ ] `SECURE_BROWSER_XSS_FILTER = True`
  - [ ] `SECURE_CONTENT_TYPE_NOSNIFF = True`
  - [ ] `X_FRAME_OPTIONS = 'DENY'`

### API Security

- [ ] Authentication required for all non-public endpoints
- [ ] Rate limiting configured
- [ ] CORS properly configured (no wildcards in production)
- [ ] Input validation on all endpoints
- [ ] SQL injection protection (using ORM properly)
- [ ] XSS protection in responses

### Frontend Security

- [ ] Environment variables not exposed in client bundle
- [ ] Content Security Policy (CSP) headers configured
- [ ] Sanitize user-generated content
- [ ] Secure cookie settings
- [ ] No sensitive data in localStorage

## 🚀 Performance

### Backend Performance

- [ ] Database queries optimized (use `select_related`, `prefetch_related`)
- [ ] Database indexes created for frequent queries
- [ ] Caching configured (Redis)
- [ ] Static files served via CDN
- [ ] Media files stored in object storage (S3)
- [ ] Compression enabled (gzip/brotli)
- [ ] Database connection pooling configured

### Frontend Performance

- [ ] Production build created (`npm run build`)
- [ ] Images optimized and using Next.js Image component
- [ ] Code splitting implemented
- [ ] Critical CSS inlined
- [ ] Fonts optimized
- [ ] Service worker for offline support (optional)

## 📊 Monitoring & Logging

### Error Tracking

- [ ] Sentry configured for both backend and frontend
- [ ] Error alerting set up
- [ ] Source maps uploaded to Sentry

### Logging

- [ ] Structured logging configured
- [ ] Log aggregation service connected (ELK, CloudWatch, etc.)
- [ ] Log levels appropriate for production
- [ ] No sensitive data in logs

### Monitoring

- [ ] Application metrics configured (Prometheus/CloudWatch)
- [ ] Health check endpoints working
- [ ] Uptime monitoring configured
- [ ] Performance monitoring enabled
- [ ] Database monitoring set up

## 🗄️ Database

- [ ] Production database backed up regularly
- [ ] Backup restoration tested
- [ ] Database migrations reviewed and tested
- [ ] Connection limits configured appropriately
- [ ] Read replicas configured (if needed)
- [ ] Database SSL enabled

## 🔧 Infrastructure

### Server Configuration

- [ ] Proper server sizing for expected load
- [ ] Auto-scaling configured (if using cloud)
- [ ] Load balancer health checks configured
- [ ] SSL certificates installed and auto-renewal configured
- [ ] Firewall rules configured
- [ ] DDoS protection enabled

### Deployment

- [ ] Zero-downtime deployment process
- [ ] Rollback procedure documented and tested
- [ ] Environment variables properly managed
- [ ] CI/CD pipeline includes all tests
- [ ] Blue-green or canary deployment (optional)

## 📋 Operational

### Documentation

- [ ] API documentation up to date
- [ ] Runbook for common issues
- [ ] Architecture diagram current
- [ ] Disaster recovery plan documented

### Team Preparedness

- [ ] On-call rotation established
- [ ] Incident response procedure defined
- [ ] Access controls properly configured
- [ ] Secrets management system in use

## 🧪 Testing

- [ ] All tests passing
- [ ] Load testing completed
- [ ] Security testing/audit performed
- [ ] User acceptance testing completed
- [ ] Rollback procedure tested

## 📱 Frontend Specific

- [ ] SEO meta tags configured
- [ ] OpenGraph tags for social sharing
- [ ] Favicon and app icons added
- [ ] PWA manifest (if applicable)
- [ ] Analytics configured
- [ ] Error boundaries implemented

## 🔄 Final Checks

- [ ] `python manage.py check --deploy` passes
- [ ] No hardcoded secrets in codebase
- [ ] All TODO/FIXME comments addressed
- [ ] Dependencies up to date
- [ ] License files included
- [ ] GDPR compliance (if applicable)

## 📈 Post-Deployment

- [ ] Monitor error rates
- [ ] Check performance metrics
- [ ] Verify backups are running
- [ ] Test critical user flows
- [ ] Monitor resource usage

---

Remember: This checklist is a starting point. Add items specific to your application and compliance requirements.
