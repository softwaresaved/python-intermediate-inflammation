"""Tests for the Patient model."""


def test_create_patient():
    from inflammation.patient import Patient

    name = 'Alice'
    patient = Patient(name=name)

    assert patient.name == name


def test_patient_inflammation():
    from inflammation.patient import Patient

    name = 'Alice'
    measurements = [0, 1, 2]
    patient = Patient(name=name)

    for meas in measurements:
        patient.add_measurement(meas)

    # Check patient measurements against reference
    for meas, ref in zip(patient.measurements, measurements):
        assert meas == ref
