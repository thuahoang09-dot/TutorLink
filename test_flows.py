import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from django.test import Client
from django.contrib.auth.models import User
from tutors.models import TutorProfile, Subject
from class_requests.models import ClassRequest
from applications.models import Application
from matched_classes.models import MatchedClass
from reviews.models import Review

def run_tests():
    print("=== BAT DAU KIEM THU TOAN BO HE THONG TUTORLINK ===")
    client = Client()

    # 1. Test Home & Public Pages
    resp = client.get('/')
    assert resp.status_code == 200, f"Home failed: {resp.status_code}"
    print("[PASS] 1. Trang chu (/) -> HTTP 200")

    resp = client.get('/tutors/')
    assert resp.status_code == 200, f"Tutors list failed: {resp.status_code}"
    print("[PASS] 2. Tim gia su (/tutors/) -> HTTP 200")

    resp = client.get('/classes/')
    assert resp.status_code == 200, f"Classes list failed: {resp.status_code}"
    print("[PASS] 3. Lop can gia su (/classes/) -> HTTP 200")

    # 2. Test Student Flow
    client.login(username='hocsinh1', password='123456')
    resp = client.get('/student/dashboard/')
    assert resp.status_code == 200, f"Student dashboard failed: {resp.status_code}"
    print("[PASS] 4. Dashboard Hoc sinh (/student/dashboard/) -> HTTP 200")

    resp = client.get('/student/posts/')
    assert resp.status_code == 200, f"Student posts failed: {resp.status_code}"
    print("[PASS] 5. Bai dang cua toi (/student/posts/) -> HTTP 200")

    resp = client.get('/student/classes/')
    assert resp.status_code == 200, f"Student classes failed: {resp.status_code}"
    print("[PASS] 6. Lop hoc cua toi (/student/classes/) -> HTTP 200")

    # Student posts a new class
    subject = Subject.objects.first()
    post_data = {
        'title': 'Test Tim gia su Toan kiem thu tu dong',
        'subject': subject.id,
        'grade': 'Lop 10',
        'location': 'Hà Nội',
        'post_province': 'Hà Nội',
        'budget': 200000,
        'budget_type': 'per_session',
        'sessions_per_week': '3 buổi/tuần',
        'schedule': 'Toi 2-4-6',
        'teaching_method': 'online',
        'description': 'Kiem thu luong dang bai tu dong'
    }
    resp = client.post('/student/post-class/', data=post_data, follow=True)
    assert resp.status_code == 200, f"Post class failed: {resp.status_code}"
    new_class = ClassRequest.objects.filter(title='Test Tim gia su Toan kiem thu tu dong').first()
    assert new_class is not None, "ClassRequest was not created"
    print(f"[PASS] 7. Hoc sinh dang bai thanh cong (ID: {new_class.id})")

    # 3. Test Tutor Flow
    tutor_u = User.objects.get(username='giasu_toan')
    tutor_u.profile.full_name = 'Gia Sư Toán'
    tutor_u.profile.save()

    tutor_prof, _ = TutorProfile.objects.get_or_create(user=tutor_u)
    tutor_prof.approval_status = 'approved'
    tutor_prof.university = 'Đại học Bách Khoa'
    tutor_prof.location = 'Hà Nội'
    tutor_prof.save()
    tutor_prof.subjects.add(subject)

    client.login(username='giasu_toan', password='123456')
    resp = client.get('/tutor/dashboard/')
    assert resp.status_code == 200, f"Tutor dashboard failed: {resp.status_code}"
    print("[PASS] 8. Dashboard Gia su (/tutor/dashboard/) -> HTTP 200")

    resp = client.get('/tutor/classes/')
    assert resp.status_code == 200, f"Tutor classes failed: {resp.status_code}"
    print("[PASS] 9. Lop dang day (/tutor/classes/) -> HTTP 200")

    # Tutor applies to the newly created class
    apply_data = {
        'proposed_price': 220000,
        'message': 'Chao em, thay rat muon nhan day lop nay.'
    }
    resp = client.post(f'/applications/apply/{new_class.id}/', data=apply_data, follow=True)
    assert resp.status_code == 200
    app = Application.objects.filter(class_request=new_class, tutor__username='giasu_toan').first()
    assert app is not None, "Application was not created"
    print(f"[PASS] 10. Gia su ung tuyen thanh cong vao lop {new_class.id}")

    # 4. Student accepts application -> creates MatchedClass
    client.login(username='hocsinh1', password='123456')
    resp = client.post(f'/applications/accept/{app.id}/', follow=True)
    assert resp.status_code == 200
    matched_class = MatchedClass.objects.filter(class_request=new_class).first()
    assert matched_class is not None, "MatchedClass was not created"
    assert matched_class.status == 'in_progress', "MatchedClass status should be in_progress"
    print(f"[PASS] 11. Hoc sinh chap nhan ung vien -> Tu dong ghep lop (ID: {matched_class.id})")

    # 5. Complete class & review
    resp = client.post(f'/matched-classes/{matched_class.id}/complete/', follow=True)
    assert resp.status_code == 200
    matched_class.refresh_from_db()
    assert matched_class.status == 'completed'
    print(f"[PASS] 12. Danh dau hoan thanh lop hoc (ID: {matched_class.id})")

    # Student writes review
    review_data = {
        'rating': 5,
        'comment': 'Gia su day rat tot va co trach nhiem cao!'
    }
    resp = client.post(f'/reviews/create/{matched_class.id}/', data=review_data, follow=True)
    assert resp.status_code == 200
    assert Review.objects.filter(matched_class=matched_class).exists()
    print("[PASS] 13. Hoc sinh danh gia 5 sao cho gia su thanh cong")

    # 6. Test Admin Flow
    client.login(username='admin', password='admin123')
    admin_pages = [
        '/admin-dashboard/',
        '/admin-dashboard/users/',
        '/admin-dashboard/tutors/',
        '/admin-dashboard/posts/',
        '/admin-dashboard/classes/',
        '/admin-dashboard/reviews/',
        '/admin-dashboard/statistics/',
    ]
    for p in admin_pages:
        resp = client.get(p)
        assert resp.status_code == 200, f"Admin page {p} failed: {resp.status_code}"
    print("[PASS] 14. Toan bo 7 trang Quan tri vien (Admin) -> HTTP 200")

    # Admin approves pending tutor (giasu_ly)
    pending_tutor = TutorProfile.objects.filter(user__username='giasu_ly').first()
    assert pending_tutor is not None
    resp = client.post(f'/admin-dashboard/tutors/{pending_tutor.id}/approve/', data={'action': 'approve', 'feedback': 'Ho so day du hop le'}, follow=True)
    assert resp.status_code == 200
    pending_tutor.refresh_from_db()
    assert pending_tutor.approval_status == 'approved', "Tutor should be approved"
    # Cleanup test artifacts to avoid polluting database tables
    Review.objects.filter(matched_class=matched_class).delete()
    matched_class.delete()
    new_class.delete()

    print("\n=== TAT CA 15/15 BAI KIEM THU LUONG DA THANH CONG 100%! ===")

if __name__ == '__main__':
    run_tests()
