"""Tests for the Doctor model."""


def test_create_doctor():
    from inflammation.doctor import Doctor

    name = 'Alice'
    doctor = Doctor(name=name)

    assert doctor.name == name


def test_doctor_patients():
    from inflammation.doctor import Doctor
    from inflammation.patient import Patient

    name = 'Alice'
    patient_names = ['Bob', 'Carol', 'David']
    doctor = Doctor(name=name)

    # Create patients and add them to the doctor
    for patient in map(Patient, patient_names):
        doctor.add_patient(patient)

    # Check that the names of the doctor's patients are correct
    for p_name, ref in zip(map(lambda x: x.name, doctor.patients),
                           patient_names):
        assert p_name == ref
