from core.settings import BASE_DIR
import pandas as pd
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ExcelModelSerializer
from django.db import transaction
from .models import ExcelModel
from rest_framework import status




@api_view(['POST'])
def upload_data(request):
    try:
        file_path = BASE_DIR / 'test.xlsx'
        df = pd.read_excel(file_path)
        column_names = df.columns.tolist()

        avg_value = df[column_names[3]].mean()
        df[column_names[3]].fillna(avg_value, inplace=True)

        data_list = []
        for _, row in df.iterrows():
            data = ExcelModel(
                parameter_name=row[column_names[1]],
                machine_name=row[column_names[2]],
                value=row[column_names[3]],
                yesterday_date=row[column_names[5]]
            )
            data_list.append(data)

        with transaction.atomic():
            ExcelModel.objects.bulk_create(data_list)

        return Response({"message": "Data uploaded successfully."})
    except FileNotFoundError:
        return Response({"error": "File not found."}, status=status.HTTP_404_NOT_FOUND)
    
    except pd.errors.EmptyDataError:
        return Response({"error": "Excel file is empty."}, status=status.HTTP_400_BAD_REQUEST)
    
    except KeyError as e:
        return Response({"error": f"Column not found: {str(e)}"}, status=status.HTTP_400_BAD_REQUEST)
    
    except Exception as e:
        return Response({"error": f"An unexpected error occurred: {str(e)}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['GET'])
def get_latest_records(request):
    try:
        # Fetch the latest 10 records
        latest_records = ExcelModel.objects.all().order_by('-id')[:10]
        serializer = ExcelModelSerializer(latest_records, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    except Exception as e:
        return Response({"error": f"An unexpected error occurred: {str(e)}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
