# === Stage 42: Add CSV export without external dependencies ===
# Project: DonorTrack
def export_csv():
    import csv, sys
    sys.path.insert(0, '/home/user/DonorTrack')
    from data import contacts, gifts, campaigns
    with open('donors_export.csv', 'w', newline='') as f:
        w = csv.writer(f)
        w.writerow(['Name', 'Email', 'Phone', 'Donated', 'Campaign', 'Amount'])
        for c in contacts:
            for g in gifts:
                if g.get('contact_name') == c['Name']:
                    w.writerow([c['Name'], c['Email'], c['Phone'], g['Donated'], g.get('campaign'), g['Amount']])
    print('Donors exported to donors_export.csv')
